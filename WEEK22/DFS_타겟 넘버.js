function solution(numbers, target) {
  var answer = 0;

  function depthFirst(index, value) {
    if (index === numbers.length) {
      if (value === target) {
        answer++;
      }

      return;
    }

    depthFirst(index + 1, value + numbers[index]);
    depthFirst(index + 1, value - numbers[index]);
  }

  depthFirst(0, 0);

  return answer;
}

console.log(solution([1, 1, 1, 1, 1], 3));
