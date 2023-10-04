// content.js
async function convertToBlackAndWhite() {
  try {
    const input = document.title;
    const url = `https://distraction-flagger-api.vercel.app/check-distraction?input=${input}`;
    const response = await fetch(url);
    const data = await response.json();

    if (data.result === 1) {
      console.log("Not a good page!");
      document.body.style.filter = 'grayscale(100%)';
      document.body.style.border = "5px solid red";
    } else {
      console.log("No action taken");
    }
  } catch (error) {
    console.log(error);

  }
}
convertToBlackAndWhite();
