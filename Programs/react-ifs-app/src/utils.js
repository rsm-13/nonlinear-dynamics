export function randrange(start, stop, step = 1) {
    if (stop === undefined) {
        stop = start;
        start = 0;
    }
    const range = (stop - start) / step;
    return Math.floor(Math.random() * range) * step + start;
}
