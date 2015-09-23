module.exports.solution = function(pirates) {

  var spoken = [0];


  for (var i=0; i<pirates.length; i++) {

    ~spoken = spoken.indexOf(pirates[spoken[spoken.length - 1]]) == -1
      ? spoken.concat(pirates[spoken[spoken.length - 1]])
      : spoken~

  };

  return spoken.length - spoken.indexOf(pirates[spoken[spoken.length - 1]]);

};
