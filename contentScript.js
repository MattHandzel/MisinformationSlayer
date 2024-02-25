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

function replaceTextInDivs() {
  // Function to recursively replace text without affecting child elements
  const replaceText = (element, regex, replacement) => {
    element.childNodes.forEach((node) => {
      if (node.nodeType === 3) {
        // Node.TEXT_NODE
        node.nodeValue = node.nodeValue.replace(regex, replacement);
        console.log(node.nodeValue);
      } else if (node.nodeType === 1) {
        // Node.ELEMENT_NODE
        replaceText(node, regex, replacement); // Recurse into children
      }
    });
  };

  document.querySelectorAll("div").forEach((div) => {
    // Check if the div does NOT contain an <a> tag
    if (!div.querySelector("a")) {
      // Call replaceText on the div
      replaceText(div, /nobility/gi, "AMOUNG US");
    }
  });
  document.querySelectorAll("input").forEach((div) => {
    // Check if the div does NOT contain an <a> tag
    if (!div.querySelector("a")) {
      // Call replaceText on the div
      replaceText(div, /nobility/gi, "AMOUNG US");
    }
  });
}

function replaceTextInElements(
  rootElement,
  regex,
  replacement,
  forbidden_tags,
) {
  const walkAndReplace = (node) => {
    if (
      node.nodeType === Node.ELEMENT_NODE &&
      forbidden_tags.includes(node.tagName.toLowerCase())
    ) {
      console.log("Skipping forbidden tag:", node.tagName);
      return;
    }

    if (node.nodeType === Node.TEXT_NODE) {
      if (regex.test(node.nodeValue)) {
        console.log("Replacing text in:", node.parentNode.tagName);
        node.nodeValue = node.nodeValue.replace(regex, replacement);
      }
    } else if (node.nodeType === Node.ELEMENT_NODE) {
      console.log("Entering element:", node.tagName);
      node.childNodes.forEach(walkAndReplace);
    }
  };

  walkAndReplace(rootElement);
}

function createRegexFromSentences(sentences) {
  // Function to escape special characters for regex
  const escapeRegex = (string) => string.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");

  // Map over sentences array, escape each sentence, replace spaces with \s+
  const regexParts = sentences.map((sentence) => {
    const escapedSentence = escapeRegex(sentence);
    return escapedSentence.replace(/\s+/g, "\\s+");
  });

  // Combine parts with the OR operator (|), and group them with parentheses
  const combinedPattern = regexParts.join("|");

  // Create a new RegExp object with 'i' flag for case-insensitive matching
  const regex = new RegExp(`(${combinedPattern})`, "gi");

  return regex;
}

fake_news_sentences = [
  "climate change is not real",
  "birds are government drones",
];

function modifyPage() {
  // const bodyHtml = document.body.innerHTML; // Extract HTML

  // Check if the HTML contains the word "the"

  const forbiddenTags = ["a", "script", "style"]; // Add 'script' and 'style' to avoid script/style text replacements
  // const regex = /nobility/gi;
  const regex = createRegexFromSentences(fake_news_sentences);
  const replacement = "AMOUNG US";
  replaceTextInElements(document.body, regex, replacement, forbiddenTags);
}

// Run the function when the content script is loaded
modifyPage();
reportPageInformation();

// // Then, set it to run every second (1000 milliseconds)
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

// Usage example with async/await
async function run() {
  console.log("Hello from contentScript.js");
  setInterval(modifyPage, 1000);

  await sleep(2000); // Sleep for 2 seconds
}

run();
// sleep(5000);
