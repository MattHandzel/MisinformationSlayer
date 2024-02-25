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

function playGif() {
  // const gifUrl = chrome.runtime.getURL('ape.jpeg');
  const gif = document.createElement("img");
  gif.src = "https://img.itch.zone/aW1nLzk3OTkzMDYuZ2lm/original/p78Kg1.gif";
  const audio = new Audio();
  audio.preload = "auto";
  audio.src =
    "https://assets.mixkit.co/active_storage/sfx/1487/1487-preview.mp3";
  gif.style.position = "fixed";
  gif.style.top = "0";
  gif.style.left = "0";
  gif.style.width = "100%";
  gif.style.height = "100%";
  gif.style.zIndex = "9999";
  sleep(1000);
  document.body.appendChild(gif);
  try {
    // Attempt to play the audio
    audio.play();
  } catch (error) {
    console.error("Failed to play:", error);
    // Handle the error, for example, by showing a message to the user
    // or by logging the error to an error reporting service
  }
  setTimeout(() => {
    gif.remove();
  }, 600);
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

    if (node.nodeType === Node.ELEMENT_NODE) {
      const ignore = node.getAttribute('ignore');
      if (ignore=="true") {
        return;
      }
      console.log("Entering element:", node.tagName);
      node.childNodes.forEach((childNode) => walkAndReplace(childNode));
    } else if (node.nodeType === Node.TEXT_NODE) {
      if (regex.test(node.nodeValue)) {
        playGif();
        console.log("Replacing text in:", node.parentNode.tagName);
        const tempElement = document.createElement("span");
        tempElement.innerHTML = node.nodeValue.replace(regex, function (match) {
          return (
            '<b class="placeholder" original-content="' +
            match +
            '" ignore="true">PLACEHOLDER - CLICK TO REVEAL</b>'
          );
        });

        // Replace the text node with the generated HTML
        node.parentNode.replaceChild(tempElement, node);

        // Handle click event to reveal original text
        tempElement.querySelectorAll(".placeholder").forEach((placeholder) => {
          placeholder.addEventListener("click", function (event) {
            event.stopPropagation(); // Prevents click event from bubbling up to ancestor elements
            const originalContent = this.getAttribute("original-content");
            if (this.textContent.trim() !== originalContent) {
              this.textContent = originalContent;
            }
          });
        });
      }
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
  "the earth is flat", "the moon is made of cheese", "humans can fly without technology", "water boils at the same temperature as it freezes", "dinosaurs performed operas", "the internet is powered by magic", "cars run on laughter", "trees send emails", "the great wall of china was built to keep rabbits out", "lightning is afraid of commitment", "shakespeare was a group of flamingos", "the color blue doesn’t exist", "gravity is just a theory", "cats speak french", "the secret to eternal youth is in a jar of pickles"];

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

window.addEventListener('load', function () {
  run();
})

// sleep(5000);
