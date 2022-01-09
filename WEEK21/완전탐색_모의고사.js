function solution(answers) {
  var answer = [];
  let student1 = [1, 2, 3, 4, 5];
  let student2 = [2, 1, 2, 3, 2, 4, 2, 5];
  let student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  let scores = new Array(3).fill(0);

  for (let i = 0; i < answers.length; i++) {
    if (answers[i] === student1[i % 5]) {
      scores[0]++;
    }
    if (answers[i] === student2[i % 8]) {
      scores[1]++;
    }
    if (answers[i] === student3[i % 10]) {
      scores[2]++;
    }
  }

  scores.forEach((element, index) => {
    if (element === Math.max(...scores)) {
      answer.push(index + 1);
    }
  });

  return answer;
}

// console.log(solution([1, 3, 2, 4, 2]));
