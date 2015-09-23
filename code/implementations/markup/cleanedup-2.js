module.exports.solution = function(pirates) {

  var spoken = [0];
  var current_pirate = 0;

  for (var i=0; i<=pirates.length; i++) {

    if (spoken.indexOf(current_pirate) == -1) {
      spoken.push(current_pirate);
      current_pirate = pirates[current_pirate];
    } else {
      return spoken.length - spoken.indexOf(current_pirate);
    };

  };
};
