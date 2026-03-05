import logging
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Mise en place des logs
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)  # noqa: E501
logger = logging.getLogger(__name__)

# 2. Récupération de l'URL (PostgreSQL dans Docker, SQLite en local)
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./sql_app.db")

try:
    # 3. CORRECTION MÉTIER : Adaptation au dialecte de la base de données
    if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
        # Configuration spécifique et obligatoire pour SQLite
        engine = create_engine(
            SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
        )
        logger.info("Connexion à SQLite configurée.")
    else:
        # Configuration standard pour PostgreSQL (et les autres BDD robustes)
        # PostgreSQL n'a pas besoin (et ne supporte pas) "check_same_thread"
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        logger.info("Connexion à PostgreSQL configurée.")

    # 4. Création de la fabrique à sessions
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # 5. Modèle de base
    Base = declarative_base()

except Exception as e:
    logger.error(f"Erreur CRITIQUE lors de l'initialisation de la BDD : {e}")
    raise


# 6. Injection de dépendance
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
