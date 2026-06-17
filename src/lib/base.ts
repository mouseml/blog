const BASE = import.meta.env.BASE_URL;

/**
 * Build a site-absolute path that respects the configured `base` (/blog), with
 * no double slashes. url() => "/blog/", url("license/") => "/blog/license/".
 * Use for every internal link and public asset so base changes stay centralized.
 */
export function url(path = '/'): string {
  const base = BASE.replace(/\/$/, '');
  const rel = path.replace(/^\//, '');
  return rel ? `${base}/${rel}` : `${base}/`;
}
