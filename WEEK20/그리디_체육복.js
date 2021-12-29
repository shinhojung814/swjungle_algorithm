function solution(n, lost, reserve) {
  let _lost = lost.filter((element) => !reserve.includes(element));
  let _reserve = reserve.filter((element) => !lost.includes(element));

  _reserve.forEach((element) => {
    if (_lost.includes(element - 1)) {
      _lost.splice(_lost.indexOf(element - 1), 1);
    } else if (_lost.includes(element + 1)) {
      _lost.splice(_lost.indexOf(element + 1), 1);
    }
  });

  let answer = n - _lost.length;

  return answer;
}

function solution(n, lost, reserve) {
  let _lost = lost.filter((element) => !reserve.includes(element));
  let _reserve = reserve.filter((element) => !lost.includes(element));

  let setLost = [...new Set(_lost)];
  let setReserve = [...new Set(_reserve)];

  setReserve.forEach((element) => {
    if (setLost.includes(element - 1)) {
      setLost.splice(setLost.indexOf(element - 1), 1);
    } else if (setLost.includes(element + 1)) {
      setLost.splice(setLost.indexOf(element + 1), 1);
    }
  });
  let answer = n - setLost.length;

  return answer;
}
