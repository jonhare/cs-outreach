var data = ["the quick brown fox", "jumped over the lazy dog"];

function applyMap(mapfcn) {
	for (i=0; i<data.length; i++) {
		applyEmit(mapfcn(data[i]))
	}
}

function applyEmit(value) {
	console.log(value);
}

applyMap(function(value) {
	var words = value.split(" ")
	var counts = {}
	for (var i = 0; i < words.length; i++) {
		if (!counts[words[i]]) {
			counts[words[i]] = 0;
		}
		counts[words[i]]++;
	}
	return counts;
});