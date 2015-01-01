var context = new (window.AudioContext || window.webkitAudioContext)();
var biquadFilter = context.createBiquadFilter();
biquadFilter.type = "lowshelf";
biquadFilter.frequency.value = 1000;
biquadFilter.gain.value = 25;


var Sound = function(url) {
    this.timeElapsed = true;
    this.source = null;
    this.isLoaded = false;
    var request = new XMLHttpRequest();
    request.open('GET', url, true);
    request.responseType = 'arraybuffer';

    // Decode asynchronously
    request.onload = function () {
        context.decodeAudioData(request.response, function (buffer) {
            AudioBuffer = buffer;
            this.source = context.createBufferSource();
            this.source.buffer = AudioBuffer;
            this.source.connect(context.destination);
            this.isLoaded=true;
            console.log("HELLO");
        });
    };
    request.send();

};

Sound.prototype.play = function() {
    console.log(this.timeElapsed);
    console.log(this.isLoaded);
    console.log(this.source);
    if(this.timeElapsed && this.isLoaded) {
        this.source.start();
        this.timeElapsed = false;
     }
};
Sound.prototype.stop = function() {
    this.source.stop();
};

Sound.prototype.pause = function() {
    source.stop();
};














function loadSound(url, soundNum) {
  var request = new XMLHttpRequest();
  request.open('GET', url, true);
  request.responseType = 'arraybuffer';

  // Decode asynchronously
  request.onload = function() {
    context.decodeAudioData(request.response, function(buffer) {
      AudioBuffer[soundNum] = buffer;
    });
  }
    request.send();
}


function playSound(soundNum) {
    if(source[soundNum]==null) {
        source[soundNum] = context.createBufferSource();
        source[soundNum].buffer = AudioBuffer[soundNum];
        source[soundNum].connect(context.destination);
        source[soundNum].start(0);
        setTimeout(function(){
                source[soundNum]=null;
            },
            (AudioBuffer[soundNum].duration*1000))
    }
}

function stopSound(soundNum) {
    source[soundNum].stop(0);
}

function pauseSound(soundNum) {
    source[soundNum].stop(0);
}

