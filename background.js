function periodicFunction() {
  console.log("Hello from background.js");
  // alert("Hello from background.js");
}
// Call periodicFunction every 10 seconds
// console.log("Hello from background.js");
setInterval(periodicFunction, 1000);
