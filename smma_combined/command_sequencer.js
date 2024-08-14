const { Configuration, OpenAIApi } = require("openai");
const dicto = require("./interests_and_habits_objs").dicto;
const simpleDicto = require("./interests_and_habits_objs").simple_dicto;
const ast = require("abstract-syntax-tree");

const configuration = new Configuration({
  organization: "org-jcGd5pFkMs5evmbGdsLaQQgb",
  apiKey: "sk-proj-mgcSidSdj4C7vI6SDyw7T3BlbkFJchaP2gcCJB5V6uCDaaAs"
});
const openai = new OpenAIApi(configuration);

console.log("connected...");

async function product(product, productDescription) {
  const completion = await openai.createChatCompletion({
    model: "gpt-4-turbo",
    messages: [
      {
        role: "user",
        content: `${simpleDicto} \n \
        From this dictionary, which is used for search engine optimization, which categories would best fit the product '${product}' with the description ${productDescription}? \
        Be not so strict on product categories; you can give it categories where it would only kind of fit in. \n \
        Return the answer ONLY as a Python dictionary, no text in the front or the back, and in one line as a Python dictionary, no new lines or indents. \
        If you pick something nested in something, make sure that it has its parent elements all the way up. \
        Return it in the format like {"root":{"children":{"Banking & Finance":{"children":{"Avid Investors"}}}}}}\
        make sure to include the first root and children, every time an element is embedded inside another element, include it inside the children element. that is very strict`
      }
    ]
  });
  return completion.data.choices[0].message.content;
}

function recursor(inputerDict, referenceDict = dicto) {
  let inputDict;
  if (typeof inputerDict === "string") {
    inputDict = JSON.parse(inputerDict);
  } else {
    inputDict = inputerDict;
  }

  let returnList = [];
  for (let key in inputDict) {
    if (key in referenceDict) {
      let passReferenceDict = referenceDict[key];
      if (passReferenceDict.selectable_xpath) {
        returnList.push({ selectable: passReferenceDict.selectable_xpath });
      }
      if (passReferenceDict.dropdown_xpath) {
        returnList.push({ dropdown: passReferenceDict.dropdown_xpath });
      }
      if (passReferenceDict.children && inputDict[key].children) {
        returnList = returnList.concat(recursor(inputDict[key].children, passReferenceDict.children));
      }
    }
  }
  return returnList;
}

async function main(query = 'sewed blanket') {
  const ff = await product(query);
  console.log(ff);
  console.log('\n\n');
  const results = recursor(ff);
  results.forEach(x => console.log(x));
}

main();
