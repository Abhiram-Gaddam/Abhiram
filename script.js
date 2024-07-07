document.getElementById('fileInput').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const content = e.target.result;
            window.fileContent = content;
        };
        reader.readAsText(file);
    }
});

document.getElementById('sendButton').addEventListener('click', function() {
    if (window.fileContent) {
        const question = document.getElementById("textInput").value;
        fetch('http://127.0.0.1:5000/upload', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: window.fileContent, additional: question })
        }).then(response => response.json())
        .then(data => {
            console.log('Response from Python:', data);
            document.getElementById('response').textContent = data.answer;
        }).catch(error => {
            console.error('Fetch error:', error);
        });
    } else {
        console.error('No file content to send.');
    }
});
