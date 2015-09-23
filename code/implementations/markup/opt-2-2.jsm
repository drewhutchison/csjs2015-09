module.exports.solution = function(pirates) {

  var spoken = [0];


  for (var i=0; i<pirates.length; i++) {

    if (spoken.indexOf(pirates[spoken[spoken.length - 1]]) == -1) {
      spoken.push(pirates[spoken[spoken.length - 1]]);

    };
  ~};

  return spoken.length - spoken.indexOf(pirates[spoken[spoken.length - 1]]);~

};
