// DFS - 여행경로

function solution(tickets) {
  var answer = [];
  let visited = new Array(tickets.length).fill(false);

  function depthFirst(tickets, start, res, count) {
    res.push(start);

    if (count === tickets.length) {
      answer = res;
      return true;
    }

    for (let i = 0; i < tickets.length; i++) {
      if (visited[i] === false && tickets[i][0] === start) {
        visited[i] = true;

        const result = depthFirst(tickets, tickets[i][1], res, count + 1);

        if (result) {
          return true;
        }

        visited[i] = false;
        res.pop();
      }
    }

    return false;
  }

  depthFirst(arr, "ICN", [], 0);

  return answer;
}
