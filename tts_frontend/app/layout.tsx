import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'VITS-TTS-RO Model WebApp',
  description: 'Lightweight TTS frontend for my Bachelor Thesis',
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
