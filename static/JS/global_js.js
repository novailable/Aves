function textColorFromHex(hexColor, rgb) {

    var r = 0, g =0, b= 0
    if (hexColor){
         hexColor = hexColor.replace(/^#/, '');

    // Parse the hex values
    const bigint = parseInt(hexColor, 16);

    // Extract RGB values
        r = (bigint >> 16) & 255;
        g = (bigint >> 8) & 255;
        b = bigint & 255;
    }

    if (rgb){

        r = rgb[0];
        g = rgb[1];
        b = rgb[2];
    }


    const luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255;

    return luminance > 0.7 ? '#111827' : '#ffffff';
}

function showMore(show_more_btn, more_panel) {

    let morePanel = document.getElementById(more_panel),
        isPanelHidden = morePanel.classList.contains('hidden');
    console.log(isPanelHidden)
    if (isPanelHidden) {
        morePanel.classList.remove('hidden');
    }
    else {
        morePanel.classList.add('hidden');
    }
}

function inputCustomSearch(input, more_panel){

    let searchTerm = input.value.toLowerCase(),
        morePanel = document.getElementById(more_panel),
        isPanelHidden = morePanel.classList.contains('hidden'),
        items = morePanel.querySelectorAll('div');
    if (isPanelHidden) {
        morePanel.classList.remove('hidden');
    }
    console.log(searchTerm)

    items.forEach(item => {
        const text = item.textContent.toLowerCase();
        console.log(text)
        if (text.includes(searchTerm)) {
            item.classList.remove('hidden');
        } else {
            item.classList.add('hidden');
        }
    });
}