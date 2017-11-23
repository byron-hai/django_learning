function displaySubMenu(li) {
    var subMenu = li.getElementsByTagName("ul")[0];
    subMenu.style.display = "block";
}

function hideSubMenu(li) {
    var subMenu = li.getElementsByTagName("ul")[0];
    subMenu.style.display = "none";
}

function drawArc(center, tasks) {
  var canvas = document.getElementById('canvas');
  if (canvas.getContext) {
     var ctx = canvas.getContext('2d');
     var counterClockwise = false;
     var x0 = center[0];
	 var y0 = center[1];
	 var width = 18;
	 var importance = ['#ed0404', '#ed8080', '#ffc805', '#afff05', '#08a52a', '#01ffc5', '#0aeeff', '#0a94ff'];
	 var line_r = (width + 2) * tasks.length + 20;
	 var pos = [x0 + line_r + 60, y0 - line_r];  // start position of legend
	 
	 drawLine(center, line_r);
	 
     for (i = 0; i < tasks.length; i++)
	 {
	   var startAngle = ((tasks[i][1]-1) / 12) * 2 * Math.PI;
       var endAngle = ((tasks[i][2]-1) / 12) * 2 * Math.PI;
	   var radius = (tasks[i][3]) * (width + 2);
	   var color = importance[tasks[i][3]];
	   // Below three lines for drawing arc;
       ctx.beginPath();
       ctx.arc(x0, y0, radius, startAngle, endAngle, counterClockwise);
       ctx.lineWidth = (width - 2 * tasks[i][3]);
	   // Below two lines is for drawing line;
	   ctx.moveTo(pos[0], (pos[1] + (width + 10) * i));
	   ctx.lineTo((pos[0] + width * 2), (pos[1] + (width + 10) * i));

       ctx.strokeStyle = color;
	   ctx.stroke();
	 }

	 for (i = 0; i < tasks.length; i++) {
	    var px = pos[0] + width * 2 + 10;
		var py = pos[1] + (width + 10) * (i + 1) - width - 4; // minus "4" is made the text position at center position.
		ctx.font = "16px Calibri";
	    ctx.fillText(tasks[i][0], px, py);
	  }
    }
}

function drawLine(center, r) {
  var canvas = document.getElementById('canvas');
  if (canvas.getContext) {
      var ctx = canvas.getContext('2d');
	  var font = ctx.font = "18px Arial";
	  //var center = [200, 250]
	  var theta = ['0', '30', '60', '90', '120', '150', '180', '210', '240', '270', '300', '330']
	  var month = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May.', 'Jun.', 'Jul.', 'Aug.', 'Sep.', 'Oct.', 'Nov.', 'Dec.']
	  for (i = 0; i < 12; i++)
	  {
	    ctx.moveTo(center[0], center[1]);
		ctx.lineTo(center[0] + r * Math.cos(Math.PI * theta[i] / 180.0), center[1] + r * Math.sin(Math.PI * theta[i] / 180.0));
		ctx.strokeText(month[i], center[0] + (r + 30) * Math.cos(Math.PI * theta[i] / 180.0) - 16, center[1] + (r + 30) * Math.sin(Math.PI * theta[i] / 180.0));
	  }
      ctx.lineWidth = 2;
	  ctx.strokeStyle = "#0a0eff";
	  ctx.stroke();
  }
}

// format [task_id, start_month, end_month, importance_value]
//tasks = [[0, 2, 3, 2], [1, 2, 6, 4], [2, 6, 9, 3], [3, 8, 12, 1], [4, 4, 12, 5], [5, 4, 8, 3]];
//drawArc(tasks);
