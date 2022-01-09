function solution(n, times) {
  var answer = 0;
  let left = 1;
  let right = n * Math.max(...times);

  while (left <= right) {
    let mid = parseInt((left + right) / 2);
    let total = 0;

    times.forEach((time) => {
      total += parseInt(mid / time);
    });

    if (total >= n) {
      answer = mid;
      right = mid - 1;
    } else if (total < n) {
      left = mid + 1;
    }
  }

  return answer;
}
