// DFS - 여행경로

function solution(tickets) {
  var answer = [];
  let visited = new Array(tickets.length).fill(false);

  tickets.sort();

  function depthFirst(curr, count, path) {
    if (count === tickets.length && answer.length === 0) {
      answer = path;
      return;
    }

    for (let i = 0; i < tickets.length; i++) {
      if (visited[i]) continue;
      if (tickets[i][0] === curr) {
        visited[i] = true;
        depthFirst(tickets[i][1], count + 1, [...path, tickets[i][1]]);
        visited[i] = false;
      }
    }
  }
  depthFirst("ICN", 0, ["ICN"]);

  return answer;
}
