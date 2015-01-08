var context = new (window.AudioContext || window.webkitAudioContext)();
var analyser = context.createAnalyser();
var sounds = [];


function Sound(soundNum, url, buffer) {
    var self = this;
    var soundData = {
        id: soundNum,
        url: url
    };
    var temp = {
        isPlaying:false,
        isChecked:false,
        wave:Object.create(WaveSurfer),
        source: null,
        buffer:buffer
    };
    var privateMethods = {
        startPlay: function(){
            temp.source = context.createBufferSource();
            temp.source.buffer = temp.buffer;
            temp.source.connect(context.destination);

            temp.source.start(0,
                temp.wave.getCurrentTime());
            temp.wave.play();
            temp.isPlaying = true;
        },
        stopPlay:function(){
            temp.source.stop();
            temp.isPlaying=false;
        }
    };


    this.draw = function() {
        temp.wave.init({
            container: document.querySelector('#wave'.concat(soundData.id)),
            waveColor: 'rgba(255, 210, 66, 0.67)',
            progressColor: 'purple',
            scrollParent: true
        });
        temp.wave.on('finish', function () {
            temp.isPlaying = false;
        });
        self.check();
        temp.wave.load(soundData.url);
        temp.wave.setVolume(0);
        temp.isLoaded = true;
    };


    this.check = function () {
        temp.isChecked = !temp.isChecked;
    };

    this.play = function () {
        if (!temp.isPlaying) {
            privateMethods.startPlay();
        }
    };

    this.changePosition = function(){
        if(temp.isPlaying){
            setTimeout(function()
                {
                    privateMethods.stopPlay();
                    privateMethods.startPlay();
                },  1
            )
        }
    };

    this.stop = function () {
        temp.wave.stop();
        privateMethods.stopPlay();
    };

    this.pause = function () {
        temp.wave.pause();
        privateMethods.stopPlay();
    };
}


function loadSound(url, soundNum) {
  var request = new XMLHttpRequest();
  request.open('GET', url, true);
  request.responseType = 'arraybuffer';

  request.onload = function() {
    context.decodeAudioData(request.response, function(buffer) {
      sounds[soundNum] = new Sound(soundNum, url, buffer);
      sounds[soundNum].draw();
    });
  };
    request.send();
}


function deleteSounds(project_id){
    var deleteString="/delete/".concat(project_id);
    var isChanged = false;
    for(var i=0;i < sounds.length; i++){
        if(sounds[i].isChecked){
            deleteString = deleteString.concat("d"+i);
            isChanged=true;
        }
    }
    window.location.href = deleteString;

}