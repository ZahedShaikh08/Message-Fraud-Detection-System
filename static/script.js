document.getElementById('messageForm').addEventListener('submit', async e => {
  e.preventDefault();
  const msg = document.getElementById('message').value.trim();
  const resultDiv = document.getElementById('result');

  if (!msg) {
    resultDiv.textContent = 'Please enter a message.';
    return;
  }

  try {
    const resp = await fetch('/detect', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: msg })
    });
    const data = await resp.json();
    if (resp.ok) {
      resultDiv.textContent = `Result: ${data.result}`;
    } else {
      resultDiv.textContent = `Error: ${data.error}`;
    }
  } catch (err) {
    resultDiv.textContent = `Request failed: ${err}`;
  }
});
