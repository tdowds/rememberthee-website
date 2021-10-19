function clickGetRememberThee(argument) {
    document.getElementById("sign-up-button").hidden = true;
    document.getElementById("sign-up-form").hidden = false;
  }



  //Character Countdown
  document.getElementById('inputMessage').onkeyup = characterCount;
  function characterCount() {
    var container = this.nextSibling;
    if (!container || container.className !== 'counter') {
      container = document.createElement('div');
      container.className = 'counter';
      this.parentNode.insertBefore(container, this.nextSibling);
    }
    container.innerHTML = this.value.length;
  }
  characterCount({
    target: document.getElementById('counter'),
    direction: 'down',
    max: 300

  });

  function submitGetRememberTheeForm(argument) {
    const inputName = document.getElementById("inputName").value;
    const inputEmail = document.getElementById("inputEmail").value;
    const inputMessage = document.getElementById("inputMessage").value;
    const error_message = document.getElementById("error_message");

    error_message.style.padding = "10px";
    var text;
    if (inputName.length < 5) {
      text = "Please Enter a Valid Name";
      error_message.innerHTML = text;
      return false;
    }
    if (inputEmail.indexOf("@") == -1) {
      text = "Please Enter a Valid Email";
      error_message.innerHTML = text;
      return false;
    }
    else {
      const data = {
        name: inputName,
        email: inputEmail,
        message: inputMessage,
        browser: window.navigator.userAgent
      };

      fetch('/sign-up', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      })
        .then(response => response.json())
        .then(data => {
          document.getElementById("sign-up-form").hidden = true;
          document.getElementById("thank-you").hidden = false;
        })
        .catch(error => {
          console.log(error);
        });
    }
  }