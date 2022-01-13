function solution(graph, node) {
  function breadthFirst(x, y) {
    queue = new Array();
    queue.push({ x, y });

    let n = node[0];
    let m = node[1];

    let dx = [-1, 0, 1, 0];
    let dy = [0, -1, 0, 1];

    while (queue.length) {
      let { x, y } = queue.shift();
      console.log({ x, y });
      //   console.log(graph[x][y]);

      for (let i = 0; i < 4; i++) {
        let nx = x + dx[i];
        let ny = y + dy[i];
        // console.log({ nx, ny });

        if ((nx < 0) | (nx >= n) | (ny < 0) | (ny >= m)) continue;

        if (graph[nx][ny] === 0) continue;

        if (graph[nx][ny] === 1) {
          graph[nx][ny] = graph[x][y] + 1;

          queue.push({ nx, ny });
        }
      }
      console.log(queue);
    }

    let answer = graph[n - 1][m - 1];

    return answer;
  }

  return breadthFirst(0, 0);
}

console.log(
  solution(
    [
      [1, 0, 1, 0, 1, 0],
      [1, 1, 1, 1, 1, 1],
      [0, 0, 0, 0, 0, 1],
      [1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1],
    ],
    (5, 6)
  )
);
