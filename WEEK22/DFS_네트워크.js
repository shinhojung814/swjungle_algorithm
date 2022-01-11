function solution(n, computers) {
  var answer = 0;
  let visited = new Array(n).fill(false);

  function depthFirst(graph, node, visited) {
    visited[node] = true;

    graph[node].forEach((element, index) => {
      if (index !== node) {
        if ((visited[index] === false) & (element === 1)) {
          depthFirst(graph, index, visited);
        }
      }
    });
  }

  visited.forEach((element, index) => {
    if (element === false) {
      answer++;

      depthFirst(computers, index, visited);
    }
  });

  return answer;
}

console.log(
  solution(3, [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1],
  ])
);
