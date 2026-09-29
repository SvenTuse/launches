export type FileEntry = { path: string; size: number; modified: string; kind: 'document' | 'image' | 'video' | 'audio' | 'file' };
export type Project = { id: string; name: string; ticker: string; status: 'complete' | 'research' | 'template' | 'guide'; info: Record<string, string>; files: FileEntry[]; cover?: string };
export type Catalog = { projects: Project[]; storage: 'local' | 'blob'; writable: boolean };
export const fileUrl = (project: string, path: string) => `/api/file?project=${encodeURIComponent(project)}&path=${encodeURIComponent(path)}`;
export function fileKind(path: string): FileEntry['kind'] {
  if (/\.(md|txt|json|csv)$/i.test(path)) return 'document';
  if (/\.(png|jpe?g|webp|gif|avif)$/i.test(path)) return 'image';
  if (/\.(mp4|webm|mov)$/i.test(path)) return 'video';
  if (/\.(mp3|wav|ogg|m4a)$/i.test(path)) return 'audio';
  return 'file';
}
