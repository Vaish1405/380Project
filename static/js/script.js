function addAndMultiply() { 
    var x = document.getElementById('xInput').value; 
    var y = document.getElementById('yInput').value;
    
    // connection to the fetch API to secure a connection with the backend. 
    fetch('/add-and-multiply', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json' // this has to specify the format information is being sent in
        },
        body: JSON.stringify({ 'x': x, 'y': y}) // putting the values in the collection and making it a string
    })
    .then(response => response.json()) 
    .then(data => {document.getElementById('output').value = data.result;}) // handle the action that you want to take care of
    .catch(error => console.error('Error:', error)); // print the error message if there is any
} 