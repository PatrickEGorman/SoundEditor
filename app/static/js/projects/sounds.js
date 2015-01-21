var context = new (window.AudioContext || window.webkitAudioContext)();
var analyser = context.createAnalyser();
var sounds = [];
var soundsViewModel = new SoundsViewModel();
var numSounds = 0;


function Sound(soundNum, url, buffer, filename) {
    var self = this;
    self.soundData = {
        id: soundNum,
        url: url,
        filename:filename
    };
    
    self.isPlaying = false;
    self.isChecked=false;
    self.source = null;
    self.buffer = buffer;
    self.className = "wave"+self.soundData.id;
    self.wave= Object.create(WaveSurfer);


    var privateMethods = {
        startPlay: function(){
            self.source = context.createBufferSource();
            self.source.buffer = self.buffer;
            self.source.connect(context.destination);

            self.source.start(0,
                self.wave.getCurrentTime());
            self.wave.play();
            self.isPlaying = true;
        },
        stopPlay:function(){
            self.source.stop();
            self.isPlaying=false;
        }
    };


    self.draw = function() {
        self.wave.init({
            container: document.querySelector("."+self.className),
            waveColor: 'rgba(255, 210, 66, 0.67)',
            progressColor: 'purple',
            scrollParent: true
        });
        self.wave.on('finish', function () {
            self.isPlaying = false;
        });
        self.wave.load(self.soundData.url);
        self.wave.setVolume(0);
        self.isLoaded = true;
    };

    self.play = function () {
        if (!self.isPlaying) {
            privateMethods.startPlay();
        }
    };

    self.changePosition = function(){
        if(self.isPlaying){
            setTimeout(function()
                {
                    privateMethods.stopPlay();
                    privateMethods.startPlay();
                },  1
            )
        }
    };

    self.stop = function () {
        self.wave.stop();
        privateMethods.stopPlay();
    };

    self.pause = function () {
        self.wave.pause();
        privateMethods.stopPlay();
    };
}

function SoundsViewModel() {
    var self = this;
    self.sounds = ko.observableArray([]);

    self.addSound = function(sound) {
        self.sounds.push(sound);
        sound.draw();
    };

    self.removeSounds = iterateSounds(function(sound){
        if(sound.isChecked){
            self.sounds.remove(sound);
        }
    });
}


function loadSound(url, soundNum, filename) {
  var request = new XMLHttpRequest();
  request.open('GET', url, true);
  request.responseType = 'arraybuffer';

  request.onload = function() {
    context.decodeAudioData(request.response, function(buffer) {
      var sound = new Sound(soundNum, url, buffer, filename);
      soundsViewModel.addSound(sound);
      numSounds++;
    });
  };
    request.send();
}


ko.applyBindings(soundsViewModel);


function iterateSounds(func){
    for(var i=0;i < sounds.length; i++){
        func(sounds[i]);
    }
}