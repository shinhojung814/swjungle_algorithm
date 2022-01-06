function solution(n, edge) {
  let visited = new Array(n + 1).fill(-1);
  let queue = new Array();
  let adjacent = new Array(n + 1).fill(null).map(() => Array());

  visited[0] = 0;
  visited[1] = 0;
  queue.push(1);

  for (let i of edge) {
    adjacent[i[0]].push(i[1]);
    adjacent[i[1]].push(i[0]);
  }

  while (queue.length) {
    let node = queue.shift();

    if (adjacent[node]) {
      adjacent[node].forEach((element) => {
        if (visited[element] === -1) {
          queue.push(element);
          visited[element] = visited[node] + 1;
        }
      });
    }
  }

  let maxDistance = Math.max(...visited);
  let answer = visited.filter((element) => element === maxDistance).length;

  return answer;
}
