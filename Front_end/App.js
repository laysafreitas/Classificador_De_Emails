document.getElementById('emailForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const emailText = document.getElementById('emailInput').value;
    const loadingMessage = document.getElementById('loadingMessage');
    const classificationResult = document.getElementById('classificationResult');
    const responseResult = document.getElementById('responseResult');

    classificationResult.textContent = 'Processando...';
    responseResult.textContent = 'Processando...';
    loadingMessage.style.display = 'block';

    const backendUrl = 'http://127.0.0.1:8000/process_email/';

    try {
        const response = await fetch(backendUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email_text: emailText })
        });

        if (!response.ok) throw new Error(`Erro do servidor: ${response.status}`);

        const result = await response.json();
        classificationResult.textContent = result.classification || 'Erro ao classificar';
        responseResult.textContent = result.suggested_response || 'Erro ao gerar resposta';
    } catch (error) {
        classificationResult.textContent = 'ERRO DE CONEXÃO';
        responseResult.textContent = `Não foi possível conectar ao servidor FastAPI. Detalhe: ${error.message}`;
    } finally {
        loadingMessage.style.display = 'none';
    }
});
