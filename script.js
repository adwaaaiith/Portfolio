const revealItems = document.querySelectorAll(".reveal");

const revealOnScroll = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
      }
    });
  },
  {
    threshold: 0.16,
  }
);

revealItems.forEach((item) => revealOnScroll.observe(item));

const simpleOperation = document.querySelector("#simple-operation");
const simpleFirst = document.querySelector("#simple-first");
const simpleSecond = document.querySelector("#simple-second");
const simpleSecondWrap = document.querySelector("#simple-second-wrap");
const simpleRun = document.querySelector("#simple-run");
const simpleResult = document.querySelector("#simple-result");
const singleNumberOperations = ["sqrt", "sin", "cos", "tan", "log10", "ln", "percentage", "factorial"];

function updateSimpleInputs() {
  if (!simpleOperation || !simpleSecondWrap) {
    return;
  }

  simpleSecondWrap.style.display = singleNumberOperations.includes(simpleOperation.value) ? "none" : "block";
}

function getFactorial(number) {
  let answer = 1;

  for (let count = 2; count <= number; count += 1) {
    answer *= count;
  }

  return answer;
}

function runSimpleCalculator() {
  const first = Number(simpleFirst.value);
  const second = Number(simpleSecond.value);
  const selected = simpleOperation.value;
  let answer;

  if (!Number.isFinite(first)) {
    simpleResult.textContent = "Please enter the first number.";
    return;
  }

  if (!singleNumberOperations.includes(selected) && !Number.isFinite(second)) {
    simpleResult.textContent = "Please enter the second number.";
    return;
  }

  if (selected === "add") answer = first + second;
  if (selected === "subtract") answer = first - second;
  if (selected === "multiply") answer = first * second;
  if (selected === "divide") answer = second !== 0 ? first / second : "Cannot divide by zero.";
  if (selected === "power") answer = first ** second;
  if (selected === "sqrt") answer = first >= 0 ? Math.sqrt(first) : "Cannot find square root of a negative number.";
  if (selected === "sin") answer = Math.sin((first * Math.PI) / 180);
  if (selected === "cos") answer = Math.cos((first * Math.PI) / 180);
  if (selected === "tan") answer = Math.tan((first * Math.PI) / 180);
  if (selected === "log10") answer = first > 0 ? Math.log10(first) : "Log is only for positive numbers.";
  if (selected === "ln") answer = first > 0 ? Math.log(first) : "Natural log is only for positive numbers.";
  if (selected === "percentage") answer = first / 100;
  if (selected === "factorial") {
    answer = first >= 0 && Number.isInteger(first) ? getFactorial(first) : "Factorial needs a non-negative whole number.";
  }
  if (selected === "round") answer = Number.isInteger(second) ? Number(first.toFixed(second)) : "Second number should be decimal places.";

  simpleResult.textContent = `Result: ${answer}`;
}

if (simpleOperation && simpleRun) {
  updateSimpleInputs();
  simpleOperation.addEventListener("change", updateSimpleInputs);
  simpleRun.addEventListener("click", runSimpleCalculator);
}
