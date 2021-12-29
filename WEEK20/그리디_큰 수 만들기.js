function solution(number, k) {
  let stack = new Array();
  let count = 0;

  for (let i = 0; i < number.length; i++) {
    const num = number[i];

    if (count === k) {
      stack.push(num);
      continue;
    }

    if (stack.length === 0) {
      stack.push(num);
    } else {
      if (stack[stack.length - 1] >= num) {
        stack.push(num);
      } else {
        while (stack[stack.length - 1] < num) {
          count += 1;
          stack.pop();

          if (count === k) break;
          if (stack.length === 0) break;
        }
        stack.push(num);
      }
    }
    if (count !== k) {
      answer = stack.slice(0, number.length - k).join("");
    }
  }
  answer = stack.join("");

  return answer;
}
