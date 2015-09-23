module.exports.solution = function(pirates) {

  var spoken = [0];
  var current_pirate = pirates[0];

  for (var i=0; i<pirates.length; i++) {

    if (spoken.indexOf(~pirates[spoken[spoken.length - 1]]~) == -1) {
      spoken.push(~pirates[spoken[spoken.length - 1]]~);
      current_pirate = pirates[~pirates[spoken[spoken.length - 1]]~];
    } else {
      return spoken.length - spoken.indexOf(~pirates[spoken[spoken.length - 1]]~);
    };

  };
};
