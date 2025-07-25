# Keylogger em Python
### Este projeto é um keylogger simples desenvolvido em Python com o propósito estritamente educacional e de estudo. Ele demonstra como a captura de teclas e a exfiltração de dados podem ser realizadas, visando o aprimoramento do conhecimento em segurança cibernética e a conscientização sobre as técnicas utilizadas em ataques reais.

<br>

### ⚠️ AVISO IMPORTANTE ⚠️
* O uso de keyloggers sem consentimento explícito e prévio do proprietário do sistema é ilegal e antiético. Este projeto foi criado APENAS para fins de pesquisa e aprendizado sobre cibersegurança e forense digital.

* NÃO utilize este código em qualquer sistema sem permissão total e informada. O desenvolvedor deste código não se responsabiliza por qualquer uso indevido.

<br>

### 🎯 Funcionalidades
* Captura de Teclas: Registra as teclas digitadas pelo usuário (letras, números, símbolos e teclas especiais como Enter, Backspace, Tab, Espaço).

* Armazenamento Local: Salva as teclas capturadas em um arquivo de log local (key_logs.txt) para persistência.

* Parada Segura: O keylogger pode ser encerrado pressionando a tecla ESC, enviando os logs finais antes de parar.

<br>

### ⚙️ Como Funciona
* O keylogger utiliza a biblioteca pynput para escutar os eventos de teclado do sistema operacional. As teclas capturadas são adicionadas a um buffer interno e também gravadas em um arquivo de texto local.