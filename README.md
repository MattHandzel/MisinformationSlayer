#### TODOs:

- Do we want to "slash" images (do what instagram does)
- Decide the scope of this project (we could also make it so that it slashes "hateful" information, or things along these lines)
- Create the popup.html file which will have some UI that looks very pretty
- Figure out how to spot "bad" information.
- Make the chrome extension part that interfaces with the "bad" information finder.
- Make a background.js that will run and try to detect stuff.
- UI stuff, favicon.
- make it so that the find and replace does not replace other things that are crucial for the website to work.

#### Resoruces:

- Extensions that are simmilar to this: https://thetrustedweb.org/browser-extensions-to-detect-and-avoid-fake-news/
- Chrome extension documentation: https://developer.chrome.com/docs/extensions/get-started/
- Development documentation: https://developer.chrome.com/docs/extensions/develop

#### Information i think is useful that i got off chatgpt

_Q: What is the purpose of background.js and popup.html in the context of Chrome extension development?_

```
In the context of Chrome extension development, background.js and popup.html serve distinct purposes and play essential roles in the functionality and user interaction of the extension.

background.js (Background Script)
The background.js file is used for the background script of a Chrome extension, which runs in the background, separate from the web page. Background scripts are designed to handle browser-level events, manage extension behavior across different tabs, and maintain state or data that needs to persist beyond the lifecycle of a specific web page or the extension's popup.

Key Uses of background.js:

Listening for Browser Events: Handling browser actions like clicks on the extension's icon, keyboard shortcuts, or other browser-triggered events.
Persistent State Management: Keeping track of data or state that needs to persist across different pages or browser sessions. This could include settings, authentication tokens, or other extension-specific data.
Background Tasks: Performing tasks in the background, like fetching data from APIs, timer-based notifications, or any processing that doesn't need direct interaction with the web page or the user.
Inter-Component Messaging: Facilitating message passing between the popup, content scripts, and the background script, allowing different parts of the extension to communicate and coordinate actions.
popup.html (Popup UI)
The popup.html file is used to define the HTML structure of the popup that appears when a user clicks on the extension's icon in the Chrome toolbar. This popup acts as the main user interface for the extension, allowing users to interact with the extension's features directly.

Key Uses of popup.html:

User Interface: Providing a graphical interface for the extension's features. This can include buttons, links, input fields, and other interactive elements.
Displaying Information: Showing data or feedback to the user, such as the results of an extension's operation, user settings, or other relevant information.
User Input and Interaction: Collecting input from the user, such as preferences, configurations, or any form of user feedback that affects how the extension operates.
Both background.js and popup.html are essential for creating a fully functional Chrome extension, with background.js handling the behind-the-scenes logic and popup.html providing the front-end interface for user interaction. Together, they enable developers to build extensions that are interactive, stateful, and responsive to browser events.
```
