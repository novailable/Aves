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

    return luminance > 0.5 ? '#111827' : '#ffffff';
}