Aqui está o README nas duas versões: Português e Inglês.

---

# YouTube Music Downloader (FLVTO Automation)

## Português 🇧🇷

Este projeto é um script automatizado em Python, utilizando Selenium, para baixar músicas do YouTube por meio do site [FLVTO](https://flvto.site/). Ele lê URLs de um arquivo de texto e automatiza o processo de conversão e download de músicas. Além disso, há um Jupyter Notebook incluído no repositório, usado para testes e aprendizado da biblioteca Selenium.

### Funcionalidades

- Automatiza o processo de conversão de vídeos do YouTube em MP3.
- Lê URLs de um arquivo de texto (`musica.txt`), onde cada linha contém um link de vídeo do YouTube.
- Interage com o site FLVTO para realizar o download das músicas convertidas.
- Fecha automaticamente as abas pop-up abertas durante o processo.

### Pré-requisitos

Antes de executar o script, certifique-se de ter instalado:

- Python 3.x
- Google Chrome
- ChromeDriver compatível com sua versão do Chrome
- Bibliotecas Python necessárias (instaláveis via pip):
  - `selenium`

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Certifique-se de que o caminho para o `chromedriver.exe` esteja correto no código:
   ```python
   chrome_driver_path = r'C:\seu-caminho\chromedriver.exe'
   ```

4. Crie um arquivo `musica.txt` no diretório `url/` e adicione os links dos vídeos do YouTube, com um link por linha.

### Uso

Execute o script Python:

```bash
python download_music.py
```

O programa irá:

- Ler os URLs do arquivo `musica.txt`.
- Navegar até o site FLVTO.
- Inserir cada URL no campo de conversão.
- Baixar o arquivo MP3 gerado.

### Testes e Desenvolvimento

Se preferir, você pode usar o Jupyter Notebook incluído para testar trechos de código e aprender a manipular o Selenium. O notebook documenta o processo de desenvolvimento e pode ser útil para ajustes.

Para abrir o notebook, execute:

```bash
jupyter notebook
```

### Observações

- Caso haja erros relacionados a pop-ups ou problemas de interação com o botão de download, revise o seletor utilizado (ID, CSS, ou XPATH) para garantir que está correto.
- Certifique-se de que o Chrome e o ChromeDriver estejam atualizados e compatíveis.

### Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## English 🇬🇧

This project is an automated Python script using Selenium to download music from YouTube via the [FLVTO](https://flvto.site/) site. It reads URLs from a text file and automates the process of converting and downloading songs. Additionally, there is a Jupyter Notebook included in the repository, used for testing and learning the Selenium library.

### Features

- Automates the process of converting YouTube videos to MP3.
- Reads URLs from a text file (`musica.txt`), where each line contains a YouTube video link.
- Interacts with the FLVTO website to download the converted songs.
- Automatically closes pop-up tabs opened during the process.

### Prerequisites

Before running the script, make sure you have installed:

- Python 3.x
- Google Chrome
- ChromeDriver compatible with your Chrome version
- Necessary Python libraries (installable via pip):
  - `selenium`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure that the path to `chromedriver.exe` is correct in the code:
   ```python
   chrome_driver_path = r'C:\your-path\chromedriver.exe'
   ```

4. Create a `musica.txt` file in the `url/` directory and add YouTube video links, one per line.

### Usage

Run the Python script:

```bash
python download_music.py
```

The program will:

- Read the URLs from the `musica.txt` file.
- Navigate to the FLVTO site.
- Insert each URL into the conversion field.
- Download the generated MP3 file.

### Testing and Development

If you prefer, you can use the included Jupyter Notebook to test code snippets and learn how to manipulate Selenium. The notebook documents the development process and can be helpful for adjustments.

To open the notebook, run:

```bash
jupyter notebook
```

### Notes

- If there are errors related to pop-ups or issues interacting with the download button, review the selector used (ID, CSS, or XPATH) to ensure it is correct.
- Ensure that Chrome and ChromeDriver are updated and compatible.

### License

This project is licensed under the [MIT License](LICENSE).

---

