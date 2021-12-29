// 스택/큐 - 기능개발

function solution(progresses, speeds) {
  var answer = [];
  let days = 0;
  let count = 0;

  while (progresses.length) {
    if (progresses[0] + days * speeds[0] >= 100) {
      progresses.shift(0);
      speeds.shift(0);
      count++;
    } else {
      if (count > 0) {
        answer.push(count);
        count = 0;
      }
      days++;
    }
  }

  answer.push(count);

  return answer;
}
