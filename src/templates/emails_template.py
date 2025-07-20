from src.templates.email_table_style import EMAIL_TABLE_STYLE

def email_template(title: str, table_html: str, resume) -> str:
    return f"""
        <html>
            <head>{EMAIL_TABLE_STYLE}</head>
            <body>
                <div class="container">
                    <div class="banner">
                        <img src="https://chatgpt.com/s/m_687bca58ce5c81918908c20c143624c9" alt="Mailman Automator Bot" />
                    </div>
                    <div class="header">
                        <h1>{title}</h1>
                    </div>   
                </div>
                <div class="content">
                    {table_html}
                </div>
                <div>
                    {resume}
                </div>
                <div class="footer">
                    Este é um e-mail automático. Não responda esta mensagem.
                </div>

            </body>
        </html>
    """