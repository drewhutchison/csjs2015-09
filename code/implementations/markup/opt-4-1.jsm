module.exports.solution = function(pirates) {

  var spoken = pirates.reduce(
    function(spoken) {
      return spoken.indexOf(pirates[spoken[spoken.length - 1]]) == -1
        ? spoken.concat(pirates[spoken[spoken.length - 1]])
        : spoken
    }, [0]
  );





  return spoken.length - spoken.indexOf(pirates[spoken~[spoken.length - 1]~]);

};
