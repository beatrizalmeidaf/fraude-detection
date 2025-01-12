import os 
import subprocess
from dotenv import load_dotenv

load_dotenv()

def download_dataset(dataset_name:str, dataset_path:str):
    """
    A função download_dataset é responsável por realizar o download do dataset na plataforma
    Kaggle. Para isso, a função utiliza a biblioteca subprocess para executar o comando kaggle

    Args:
    dataset_name (str): Nome do dataset a ser baixado
    dataset_path (str): Caminho onde o dataset será salvo
    """
    # Obtém as credenciais da API Kaggle nas variáveis de ambiente
    kaggle_username = os.getenv("KAGGLE_USERNAME")
    kaggle_key = os.getenv("KAGGLE_KEY")

    # Define as credenciais da API Kaggle
    os.environ["KAGGLE_USERNAME"] = kaggle_username
    os.environ["KAGGLE_KEY"] = kaggle_key

    try:
        subprocess.run(["kaggle", "datasets", "download", "-d", dataset_name, "-p", dataset_path, "--unzip"], check=True)
        print(f"Dataset {dataset_name} baixado com sucesso em `{dataset_path}!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao baixar o dataset {dataset_name}: {e}")


if __name__ == "__main__":
    dataset_name = "mlg-ulb/creditcardfraud"
    dataset_path = "../../data"
    download_dataset(dataset_name, dataset_path)

