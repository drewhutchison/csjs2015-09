module.exports.solution = function(pirates) {
  return pirates.reduce(
    function(spoken) {
      return spoken.indexOf(pirates[spoken[spoken.length - 1]]) == -1
        ? spoken.concat(pirates[spoken[spoken.length - 1]])
        : spoken
    }, [0]
  ).length - pirates.reduce(
    function(spoken) {
      return spoken.indexOf(pirates[spoken[spoken.length - 1]]) == -1
        ? spoken.concat(pirates[spoken[spoken.length - 1]])
        : spoken
    }, [0]
  ).indexOf(pirates[
    pirates.reduce(
      function(spoken) {
        return spoken.indexOf(pirates[spoken[spoken.length - 1]]) == -1
          ? spoken.concat(pirates[spoken[spoken.length - 1]])
          : spoken
      }, [0]
    ).slice(-1)[0]]
  );
};
