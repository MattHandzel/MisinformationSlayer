// Function to extract all text from the page
function extractText() {
  return document.body.innerText;
}

// Function to extract all image sources from the page
function extractImages() {
  const images = document.querySelectorAll("img");
  const imageSources = Array.from(images).map((img) => img.src);
  return imageSources;
}

// Function to report extracted information
function reportPageInformation() {
  // alert("Hello from reportPageInformation");
  const text = extractText();
  const images = extractImages();

  console.log("Extracted Text:", text);
  console.log(
    "Extracted Images:",
    images.length > 0 ? images : "No images found.",
  );

  // Here you can add functionality to send this data somewhere, like to your server or log it
}

function modifyPage() {
  const bodyHtml = document.body.innerHTML; // Extract HTML

  // Check if the HTML contains the word "the"
  if (true) {
    // Example modification: Replace "the" with "THE"
    const modifiedHtml = bodyHtml.replace(/the/gi, "tAUMOUNG useo"); // somple modification
    document.body.innerHTML = modifiedHtml; // Update the page HTML
    // alert("amoung is");
  }
}

// Run the function when the content script is loaded
modifyPage();
reportPageInformation();
// alert("Hello from contentScript.js");
// Run the report function on page load
// window.addEventListener("load", reportPageInformation);
