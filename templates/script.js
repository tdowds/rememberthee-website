// function clickGetRememberThee(argument) {
//     document.getElementById("sign-up-button").hidden = true;
//     document.getElementById("sign-up-form").hidden = false;
//   }

//   function submitGetRememberTheeForm(argument) {
//     const data = {
//       name: document.getElementById('inputName').value,
//       email: document.getElementById('inputEmail').value,
//       message: document.getElementById('inputMessage').value,
//       browser: window.navigator.userAgent
//     };

//     fetch('/sign-up', {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json'
//       },
//       body: JSON.stringify(data)
//     })
//     .then(response => response.json())
//     .then(data => {
//       document.getElementById("sign-up-form").hidden = true;
//       document.getElementById("thank-you").hidden = false;
//     })
//     .catch(error => {
//       console.log(error);
//     });
//   }


// //   function validateForm() {
// //     let x = document.forms["sign-up"]["fullName"].value;
// //     if (x == "") {
// //       alert("Name must be filled out");
// //       return false;
// //     }
// //   }

// // function validateEmail() {
// //     var emailID = document.myForm.EMail.value;
// //     atpos = emailID.indexOf("@");
// //     dotpos = emailID.lastIndexOf(".");

// //     if (atpos < 1 || ( dotpos - atpos < 2 )) {
// //        alert("Please enter correct email ID")
// //        document.myForm.EMail.focus() ;
// //        return false;
// //     }
// //     return( true );
// //  }