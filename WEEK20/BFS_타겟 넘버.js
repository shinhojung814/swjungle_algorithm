// BFS - 타겟 넘버

function solution(numbers, target) {
  var answer = 0;

  function depthFirst(idx, value) {
    if (idx === numbers.length) {
      if (value === target) {
        answer += 1;
      }
      return;
    }
    depthFirst(idx + 1, value + numbers[idx]);
    depthFirst(idx + 1, value - numbers[idx]);
  }

  depthFirst(0, 0);

  return answer;
}

console.log(solution([1, 1, 1, 1, 1], 3));
