/**
 * Our name in running text, never without our mark, as the site draws it (Regards.svelte in the app): the mark
 * just before the word, 1.1em, on its baseline, the two never breaking apart; at night it turns over (light
 * lines on dark), as the site's .ink-art does. `domain` writes regards.design.
 * Titles, meta text, links' URLs and code stay plain.
 */
export const Regards = ({ domain = false }) => (
  <span style={{ whiteSpace: 'nowrap' }}>
    <img
      src="/logo/mark.svg"
      alt=""
      noZoom
      className="regards-mark"
      style={{ display: 'inline-block', width: '1.1em', height: '1.1em', margin: '0 0.22em 0 0.04em', verticalAlign: '-0.22em', borderRadius: 0, boxShadow: 'none' }}
    />
    {domain ? 'regards.design' : 'regards'}
  </span>
);
