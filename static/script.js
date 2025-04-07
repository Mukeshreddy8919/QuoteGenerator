function generateQuote() {
    fetch('/get_quote?ts=' + new Date().getTime(), {
      method: 'POST'
    })
    .then(res => res.json())
    .then(data => {
      document.getElementById('quote-box').innerText = data.reply;
    })
    .catch(err => {
      document.getElementById('quote-box').innerText = "Oops! Something went wrong.";
      console.error(err);
    });
  }
  
  