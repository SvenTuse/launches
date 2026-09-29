import type { Metadata } from 'next';
import './globals.css';
export const metadata: Metadata = { title: "Research Lounge — Research workspace", description: 'Private case study research library', robots: { index: false, follow: false } };
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return <html lang="en"><body>{children}</body></html>;
}
