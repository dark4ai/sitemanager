var RTOOLBAR = {
	html: { name: 'html', title: RLANG.html, func: 'toggle' },	
	separator10: { name: 'separator' },		
	fullscreen: { name: 'fullscreen', title: RLANG.fullscreen, func: 'fullscreen' },	
	separator11: { name: 'separator' },	
	undo:   {exec: 'Undo', name: 'undo', title: RLANG.undo },
	//redo: 	{exec: 'Redo', name: 'redo', title: RLANG.redo},	
	separator1: { name: 'separator' },			
	styles: 
	{
		name: 'styles', title: RLANG.styles, func: 'show', 
		dropdown: 
		{
			p: 			{exec: 'formatblock', name: '<p>', title: RLANG.paragraph},
			blockquote: {exec: 'formatblock', name: '<blockquote>', title: RLANG.quote},
			code: 		{exec: 'formatblock', name: '<pre>', title: RLANG.code},
			h2: 		{exec: 'formatblock', name: '<h2>', title: RLANG.header1, style: 'font-size: 18px;'},
			h3: 		{exec: 'formatblock', name: '<h3>', title: RLANG.header2, style: 'font-size: 14px; font-weight: bold;'}																	
		}
	},				
	format: 
	{
		name: 'format', title: RLANG.format, func: 'show',
		dropdown: 
		{
			bold: 		  {exec: 'bold', name: 'bold', title: RLANG.bold, style: 'font-weight: bold;'},
			italic: 	  {exec: 'italic', name: 'italic', title: RLANG.italic, style: 'font-style: italic;'},
			superscript:  {exec: 'superscript', name: 'superscript', title: RLANG.superscript},
			strikethrough:  {exec: 'StrikeThrough', name: 'StrikeThrough', title: RLANG.strikethrough, style: 'text-decoration: line-through !important;'},
		}						
	},
	separator3: { name: 'separator' },			
	lists: 	
	{
		name: 'lists', title: RLANG.lists, func: 'show',
		dropdown: 
		{
			ul: 	 {exec: 'insertunorderedlist', name: 'insertunorderedlist', title: '&bull; ' + RLANG.unorderedlist},
			ol: 	 {exec: 'insertorderedlist', name: 'insertorderedlist', title: '1. ' + RLANG.orderedlist},
			outdent: {exec: 'outdent', name: 'outdent', title: '< ' + RLANG.outdent},
			indent:  {exec: 'indent', name: 'indent', title: '> ' + RLANG.indent}
		}			
	},
	align: 	
	{
		name: 'align', title: RLANG.align, func: 'show',
		dropdown: 
		{
			JustifyLeft: 	 {exec: 'JustifyLeft', name: 'JustifyLeft', title: RLANG.align_left},					
			JustifyCenter: 	 {exec: 'JustifyCenter', name: 'JustifyCenter', title: RLANG.align_center},
			JustifyRight: {exec: 'JustifyRight', name: 'JustifyRight', title: RLANG.align_right}
		}		
	},	
	separator5: { name: 'separator' },
	image: { name: 'image', title: RLANG.image, func: 'showImage' },
	video: { name: 'video', title: RLANG.video, func: 'showVideo' },
	table: { name: 'table', title: RLANG.table, func: 'showTable' },
	separator6: { name: 'separator' },
	link: 
	{
		name: 'link', title: RLANG.link, func: 'show',
		dropdown: 
		{
			link: 	{name: 'link', title: RLANG.link_insert, func: 'showLink'},
			unlink: {exec: 'unlink', name: 'unlink', title: RLANG.unlink}
		}			
	},
	removeformat: {exec: 'removeformat', name: 'format_clean', title: RLANG.removeformat}
};
